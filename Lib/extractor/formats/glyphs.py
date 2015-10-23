import os
import shutil
import tempfile


def isGlyphs(pathOrFile):
    if not isinstance(pathOrFile, basestring):
        return False
    if os.path.splitext(pathOrFile)[-1].lower() != ".glyphs":
        return False
    return True


def extractFontFromGlyphs(
        pathOrFile, destination, doGlyphs=True, doInfo=True, doKerning=True,
        doGroups=True, doFeatures=True, doLib=True, customFunctions=[]):

    from glyphs2ufo.glyphslib import load_to_ufos

    ufoPath = tempfile.mkdtemp(suffix=".ufo")
    fonts = load_to_ufos(pathOrFile)
    fonts[0].save(ufoPath)
    try:
        extractFontFromUFO(ufoPath, destination,
            doGlyphs=doGlyphs, doInfo=doInfo,
            doKerning=doKerning, doGroups=doGroups,
            doFeatures=doFeatures, doLib=doLib,
            customFunctions=customFunctions
        )
    finally:
        shutil.rmtree(ufoPath)
