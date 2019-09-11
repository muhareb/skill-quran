# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.


import random
from os.path import dirname, join

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.audioservice import AudioService
from mycroft.audio import wait_while_speaking

from . import utils

class QuranSkill(MycroftSkill):
    def __init__(self):
        super(QuranSkill, self).__init__(name="QuranSkill")
        self.process = None

    def initialize(self):
        self.audioservice = AudioService(self.bus)

###################################################################
    @intent_file_handler('surah.intent')
    def handle_surah_intent(self, message):
        article = message.data.get('surah')
        readerName  = message.data.get('reader')

        if readerName is None:
            reader=random.choice(utils.readers)
        else:
            try:
                reader_i=utils.readers_ar.index(readerName)
                reader  =utils.readers[reader_i]
            except ValueError:
                reader=random.choice(utils.readers)
                #print("reader ValueError")
 
        if article is None:
            surah=str(random.choice(range(1, 114)))
        else:
            try:
               surah=str(utils.surahs.index(article)+1)
            except ValueError:
               surah=str(random.choice(range(1, 114)))
               #print("surah ValueError")

        #print(article)
        #print(readerName)
        #print(surah)
        #print(reader)

        if readerName!="متنوع":
            url="http://api.alquran.cloud/v1/surah/"+surah+"/"+reader
            json = utils.json_from_url(url)
            path = utils.parse_surah(json)
        else:
            paths = []
            path  = []
            for reader in utils.readers:
                url ="http://api.alquran.cloud/v1/surah/"+surah+"/"+reader
                json= utils.json_from_url(url)
                paths.append(utils.parse_surah(json))
            for ii in range(len(paths[0])):                             
                path.append(paths[random.choice(range(0, 9))][ii])
                #print(path[ii])

        try:
            #self.speak_dialog('quran')
            #wait_while_speaking()
            self.audioservice.play(path)
        except Exception as e:
            self.log.error("Error: {0}".format(e))
#################################################################################
    @intent_file_handler('tafseer.intent')
    def handle_tafseer_intent(self, message):
        article = message.data.get('surah')

        if article is None:
            surah=str(random.choice(range(1, 114)))
        else:
            try:
               surah=str(utils.surahs.index(article)+1)
            except ValueError:
               surah=str(random.choice(range(1, 114)))

        #Audio
        url="http://api.alquran.cloud/v1/surah/"+surah+"/ar.alafasy"
        json = utils.json_from_url(url)
        path_surah = utils.parse_surah(json)

        #Tafseer
        #url="http://api.alquran.cloud/v1/surah/"+surah+"/editions/ar.muyassar"
        url="http://api.alquran.cloud/v1/surah/"+surah+"/editions/ar.jalalayn"

        json = utils.json_from_url(url)
        path_tafseer = utils.parse_tafseer(json)

        try:
            for ayah in range(len(path_tafseer)):
                self.audioservice.play(path_surah[ayah])
                wait_while_speaking()
                self.speak(path_tafseer[ayah])
                wait_while_speaking()
        except Exception as e:
            self.log.error("Error: {0}".format(e))

#################################################################################
    def stop(self):
        if self.process and self.process.poll() is None:
            self.speak_dialog('quran.stop')
            self.process.terminate()
            self.process.wait()


def create_skill():
    return QuranSkill()
