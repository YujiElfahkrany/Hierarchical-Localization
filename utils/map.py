import os
import sys
import tqdm, tqdm.notebook
tqdm.tqdm = tqdm.notebook.tqdm  # notebook-friendly progress bars
from pathlib import Path

from hloc import extract_features, match_features, reconstruction, visualization, pairs_from_exhaustive
from hloc.visualization import plot_images, read_image
from hloc.utils import viz_3d

def map(inputDir, outputDir, feature_conf, matcher_conf):
    images = Path(inputDir)
    outputs = Path(outputDir)

    if not os.listdir(images):
        sys.exit("Input Directory is empty... exiting")

    if os.listdir(outputs)
        sys.exit("output Directory is not empty... exiting")

    sfm_pairs = outputs / 'pairs-sfm.txt'
    loc_pairs = outputs / 'pairs-loc.txt'
    sfm_dir = outputs / 'sfm'
    features = outputs / 'features.h5'
    matches = outputs / 'matches.h5'

    references = [p.relative_to(images).as_posix() for p in (images / 'mapping/').iterdir()]
    print(len(references), "mapping images")

    extract_features.main(feature_conf, images, image_list=references, feature_path=features)
    pairs_from_exhaustive.main(sfm_pairs, image_list=references)
    match_features.main(matcher_conf, sfm_pairs, features=features, matches=matches);

    model = reconstruction.main(sfm_dir, images, sfm_pairs, features, matches, image_list=references)

    return [model, ] # continue from here 
