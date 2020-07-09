#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Bryanhu .
@Bryanhu .

Made with love by Bryanhu .

Version: v0.0.0.1

Desc: This file is for tokenizing the scratch project for
easier usage. It will store the output tokens in a TOKEN_JSON file. This is
made so other languages such as C++, etc can easily process ugly scratch JSON.
"""
################################################################
# Imports ######################################################
################################################################
import json
# import pprint  # NOT USED

################################################################
# Get input from INPUT_JSON.txt ################################
################################################################

with open('INPUT_JSON.txt') as f:
    parseme = json.loads(f.read())
output = {}

print(parseme['targets'])


class Sprite(object):
    # TODO: Simplify the assignments
    # How? Well, we're going to combine the data variables and the lists.


    def __init__(self,variables, lists, broadcasts, blocks, comments,
                costumes, sounds, volume, tempo, videoTransparency,
                videoState, textToSpeechLanguage, name, data, code):
        # Boring stuff
        # NOTE: We're not using the name, data, and code variables
        # Just yet.
        self.code                 = code
        self.broadcasts           = broadcasts
        self.lists                = lists
        self.sounds               = sounds
        self.tempo                = tempo
        self.textToSpeechLanguage = textToSpeechLanguage
        self.videoState           = videoState
        self.videoTransparency    = videoTransparency
        self.volume               = volume
        self.variables            = variables

if __debug__:
    for target in parseme['targets']:
        if (given_stage := target['isStage']):
            # There must be a better way to do this
            stage = Sprite(
                          # The data
                          {  # Processing the variables
                              variable[1][0]:variable[1][1]
                              for variable in list(
                                  given_stage['variables'].items())
                          },
                          given_stage['lists'],
                          given_stage['broadcasts'],
                          # Workspace elements
                          given_stage['blocks'],
                          given_stage['comments'],
                          given_stage['costumes'],
                          # Sounds
                          given_stage['sounds'],
                          given_stage['volume'],
                          given_stage['tempo'],
                          # Video elements
                          given_stage['videoTransparency'],
                          given_stage['videoState'],
                          given_stage['textToSpeechLanguage'])
