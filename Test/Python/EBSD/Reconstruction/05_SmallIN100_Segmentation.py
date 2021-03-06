# Pipeline : (05) SmallIN100 Segmentation (from EBSD Reconstruction)
#
#

import simpl
import simplpy as d3d
import simpl_helpers as sh
import simpl_test_dirs as sd
import reconstructionpy as reconstruction

def small_in100_segmentation():
    # Create Data Container Array
    dca = simpl.DataContainerArray()

    # Read DREAM3D File
    err = sh.ReadDREAM3DFile(dca, sd.GetBuildDirectory() + '/Data/Output/Reconstruction/04_SmallIN100_Presegmentation.dream3d')
    assert err == 0, f'Read DataContainerArray Structure Failed {err}'

    # Segment Features (Misorientation)
    err = reconstruction.ebsd_segment_features(dca, 'Grain Data', 5, True,
                                               simpl.DataArrayPath('Small IN100', 'EBSD Scan Data', 'Mask'),
                                               simpl.DataArrayPath('Small IN100', 'EBSD Scan Data', 'Phases'),
                                               simpl.DataArrayPath('Small IN100', 'Phase Data', 'CrystalStructures'),
                                               simpl.DataArrayPath('Small IN100', 'EBSD Scan Data', 'Quats'),
                                               'FeatureIds', 'Active')
    assert err == 0, f'SegmentFeatures ErrorCondition {err}'

    # Write to DREAM3D file
    err = sh.WriteDREAM3DFile(
        sd.GetBuildDirectory() + '/Data/Output/Reconstruction/05_SmallIN100_Segmentation.dream3d',
        dca)
    assert err == 0, f'WriteDREAM3DFile ErrorCondition: {err}'

if __name__ == '__main__':
    small_in100_segmentation()
