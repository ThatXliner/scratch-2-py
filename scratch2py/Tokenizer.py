#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Bryanhu .
@Bryanhu .

Made with love by Bryanhu .

Version: v0.0.0.1

Desc: This file is for tokenizing the scratch project for
easier usage. It will store the output tokens in a list called
'token_output' or in an output.txt file. These tokens may be used for
other languages to process such as C++, etc.
"""
import json
import pprint


def get_file(prompt="Please enter the full file path:"):
    """
    To easily get the contents of a file.
    Is recursive.

    Parameters
    ----------
    prompt : str
        The prompt string.

    Returns
    -------
    str
        The contents of the file.

    """

    from pathlib2 import Path

    file_path = Path(input(str(prompt))).expanduser()
    try:
        return str(file_path.read_text())
    except Exception:
        print('Invalid file path')
        return get_file(prompt=prompt)



# parseme = json.loads(get_file(prompt='Enter the path to the txt file to parse:'))

parseme = json.loads(parseme)
output = {}

print(parseme['targets'])


class Sprite(object):
    # TODO: Simplify the assignments
    def __init__(self, variables, lists, broadcasts, blocks, comments,
                 costumes, sounds, volume, tempo, videoTransparency,
                 videoState, textToSpeechLanguage, name, data, code):
        # Boring stuff
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
