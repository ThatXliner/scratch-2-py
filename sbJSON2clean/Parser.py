#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Bryanhu .

@Bryanhu .

Made with love by Bryanhu .

Version: v0.1.0.1

Desc: This file is for tokenizing the scratch project for
easier usage. It will store the output JSON in a GOOD_JSON.json file. This is
made so other languages such as C++, etc can easily process ugly scratch JSON.
"""
################################################################
# Imports ######################################################
################################################################
import json as _json
from pathlib import Path


# import pprint  # NOT USED

################################################################
# Object definitions ###########################################
################################################################

# NOTE: This is probably unnecessary


class Sprite(object):
    """Python's scratch sprites.

    Attributes
    ----------
    code
    broadcasts
    lists
    sounds
    tempo
    textToSpeechLanguage
    videoState
    videoTransparency
    volume
    variables

    """

    # TODO: Simplify the assignments
    # How? Well, we're going to combine the data variables and the lists.

    def __init__(
        self,
        json
    ):
        """For making the scratch sprites a little bit easier to handle.

        Returns
        -------
        type
            Description of returned object.

        """
        # Boring stuff
        self._name = json["name"]
        self._vars = {item[0]: item[1] for item in json["variables"].values()}
        self.code = json["blocks"]
        self.costumes = json["costumes"]
        self.sounds = json["sounds"]
        self.volume = json["volume"]
        self.layerOrder = json["layerOrder"]
        self.visible = json["visible"]
        self.x = json["x"]
        self.y = json["y"]
        self.size = json["size"]
        self.direction = json["direction"]
        self.draggable = json["draggable"]
        self.rotationStyle = json["rotationStyle"]





class WalrusDiedError(Exception):
    """You're not running the version of python that supports the walrus operator syntax."""

    pass
class Parser(object):
    def __init__(self, json):
        self._sprites = [item for item in json["targets"] if not item["isStage"]]
        self._stage = [item for item in json["targets"] if item["isStage"]][0]
        self._globals = {item[0]: item[1] for item in self._stage["variables"].values()}


################################################################
# Get input from INPUT_JSON.txt ################################
################################################################
INPUT_FILE = "INPUT_JSON.txt"

parseme = json.loads(Path(Path(__file__).parent / f"{INPUT_FILE}").read_text())
output  = {}

print(parseme["targets"])


if __debug__:
    for target in parseme["targets"]:
        if target["isStage"] :
            given_stage = target
            # There must be a better way to do this
            stage = Sprite(
                    # The data
                    {  # Processing the variables
                        variable[1][0]: variable[1][1]
                        for variable in list(given_stage["variables"].items())
                    },
                    given_stage["lists"],
                    given_stage["broadcasts"],
                    # Workspace elements
                    given_stage["blocks"],
                    given_stage["comments"],
                    given_stage["costumes"],
                    # Sounds
                    given_stage["sounds"],
                    given_stage["volume"],
                    given_stage["tempo"],
                    # Video elements
                    given_stage["videoTransparency"],
                    given_stage["videoState"],
                    given_stage["textToSpeechLanguage"],
            )
