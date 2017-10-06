# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..odf import SFPeaks


def test_SFPeaks_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    density=dict(argstr='-density %d',
    units='NA',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='-inputfile %s',
    mandatory=True,
    ),
    inputmodel=dict(argstr='-inputmodel %s',
    mandatory=True,
    ),
    mepointset=dict(argstr='-mepointset %d',
    units='NA',
    ),
    noconsistencycheck=dict(argstr='-noconsistencycheck',
    ),
    numpds=dict(argstr='-numpds %d',
    units='NA',
    ),
    order=dict(argstr='-order %d',
    units='NA',
    ),
    out_file=dict(argstr='> %s',
    genfile=True,
    position=-1,
    ),
    pdthresh=dict(argstr='-pdthresh %f',
    units='NA',
    ),
    pointset=dict(argstr='-pointset %d',
    units='NA',
    ),
    rbfpointset=dict(argstr='-rbfpointset %d',
    units='NA',
    ),
    scheme_file=dict(argstr='%s',
    ),
    searchradius=dict(argstr='-searchradius %f',
    units='NA',
    ),
    stdsfrommean=dict(argstr='-stdsfrommean %f',
    units='NA',
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    )
    inputs = SFPeaks.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_SFPeaks_outputs():
    output_map = dict(peaks=dict(),
    )
    outputs = SFPeaks.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
