from utils/check_for_query.py import checkForQueryImage
from utils/map.py import map
from utils/match.py import match

feature_conf = extract_features.confs['superpoint_aachen']
matcher_conf = match_features.confs['superglue']

periodicTimeToCheckForInput_s = 0.1
inputFolder = "input/mapping"
outputFolder = "output"
queryFolder = "query/"
queryFile = checkForQueryImage("input", periodicTimeToCheckForInput_s)

mappingResult = map(inputFolder, outputFolder, feature_conf, matcher_conf)
