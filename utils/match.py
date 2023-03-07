import os
import sys
from hloc import extract_features, match_features, reconstruction, visualization, pairs_from_exhaustive

def match(model, images, queryFolder, feature_conf, matcher_conf, features, loc_pairs, references, matches):
    if not os.listdir(queryFolder):
        sys.exit("Query Directory is empty... exiting")

    extract_features.main(feature_conf, images, image_list=[queryFolder], feature_path=features, overwrite=True)
    pairs_from_exhaustive.main(loc_pairs, image_list=[query], ref_list=references)
    match_features.main(matcher_conf, loc_pairs, features=features, matches=matches, overwrite=True);

    import pycolmap
    from hloc.localize_sfm import QueryLocalizer, pose_from_cluster

    camera = pycolmap.infer_camera_from_image(images / queryFolder)
    ref_ids = [model.find_image_with_name(r).image_id for r in references]
    conf = {
        'estimation': {'ransac': {'max_error': 12}},
        'refinement': {'refine_focal_length': True, 'refine_extra_params': True},
    }
    localizer = QueryLocalizer(model, conf)
    ret, log = pose_from_cluster(localizer, queryFolder, camera, ref_ids, features, matches)

    print(f'found {ret["num_inliers"]}/{len(ret["inliers"])} inlier correspondences.')

    pose = pycolmap.Image(tvec=ret['tvec'], qvec=ret['qvec'])
