#!/usr/bin/env python
# -*- coding: utf-8 -*-
from google.cloud import language_v1
from google.cloud.language_v1 import enums
import os
import csv
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Development-project.json"

from google.cloud import language_v1
from google.cloud.language_v1 import enums

dist_list_entity = {}
dist_list_entity_all = {}
list_type = {}
list_with_salience = []
count = {
    'person': 0,
    'other' : 0,
};
# print result
import operator
import pickle
from os import path
# define a list of places
def write_obj(name, data):
    with open(name, 'wb') as filehandle:
        # store the data as binary data stream
        pickle.dump(data, filehandle)

def read_file(file_name):
    with open(file_name, 'rb') as filehandle:
        # read the data as binary data stream
        return pickle.load(filehandle)

def sample_analyze_entities(text_content):
    """
    Analyzing Entities in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'California is a state.'

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "ja"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_entities(document, encoding_type=encoding_type)
    # Loop through entitites returned from the API
    for entity in response.entities:
        # print(u"Representative name for the entity: {}".format(entity.name))
        temp = {
            'name' : entity.name,
            'type' : enums.Entity.Type(entity.type).name,
            'salience' : entity.salience,
        }
        list_with_salience.append(temp)
        if entity.name in dist_list_entity.keys():
            dist_list_entity[entity.name] = dist_list_entity[entity.name] + 1
            dist_list_entity_all[entity.name] = dist_list_entity_all[entity.name] + text_content.count(entity.name)
        else:

            dist_list_entity[entity.name] = 1
            dist_list_entity_all[entity.name] = 0 + text_content.count(entity.name)
        if entity.name not in list_type.keys():
            list_type[entity.name] = enums.Entity.Type(entity.type).name
        if(entity.name == "方"):
            # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
            print(u"Entity type: {}".format(enums.Entity.Type(entity.type).name))
            if(enums.Entity.Type(entity.type).name == "PERSON"):
                count['person'] += 1
            if (enums.Entity.Type(entity.type).name == "OTHER"):
                count['other'] += 1
            # Get the salience score associated with the entity in the [0, 1.0] range
            # print(u"Salience score: {}".format(entity.salience))
            # # Loop over the metadata associated with entity. For many known entities,
            # # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
            # # Some entity types may have additional metadata, e.g. ADDRESS entities
            # # may have metadata for the address street_name, postal_code, et al.
            # for metadata_name, metadata_value in entity.metadata.items():
            #     print(u"{}: {}".format(metadata_name, metadata_value))
            #
            # # Loop over the mentions of this entity in the input document.
            # # The API currently supports proper noun mentions.
            # for mention in entity.mentions:
            #     print(u"Mention text: {}".format(mention.text.content))
            #     # Get the mention type, e.g. PROPER for proper noun
            #     print(
            #         u"Mention type: {}".format(enums.EntityMention.Type(mention.type).name)
            #     )

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language))

def calcu(text, entity):
    return text.count(entity)

def read_data(file_name):
    with open(file_name, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            result = sample_analyze_entities(row['text'])
            line_count = line_count + 1
            print(result)
        print('Processed  lines.', line_count)

if path.exists("data/dist_list_entity") == False:
    read_data('call_data.csv')
    dist_list_entity = sorted(dist_list_entity.items(), key=operator.itemgetter(1), reverse=True)
    print(dist_list_entity)
    dist_list_entity_all = sorted(dist_list_entity_all.items(), key=operator.itemgetter(1), reverse=True)
    list_with_salience = sorted(list_with_salience, key=lambda x: x["salience"], reverse=True)
    write_obj('data/dist_list_entity', dist_list_entity)
    write_obj('data/dist_list_entity_all', dist_list_entity_all)
    write_obj('data/list_type', list_type)
    write_obj('data/list_with_salience', list_with_salience)
else:
    print("Data exist")
    dist_list_entity = read_file('data/dist_list_entity')
    dist_list_entity_all = read_file('data/dist_list_entity_all')
    list_type = read_file('data/list_type')
    list_with_salience = read_file('data/list_with_salience')

list_ignore = []
print(count['person'])
print(count['other'])
with open('result.csv', mode='w') as write_list_entity:
    employee_writer = csv.writer(write_list_entity, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for ele in dist_list_entity:
        if list_type[ele[0]] not in list_ignore:
            employee_writer.writerow([ele[0], ele[1], list_type[ele[0]]])

with open('result2.csv', mode='w') as write_list_entity:
    employee_writer = csv.writer(write_list_entity, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for ele in dist_list_entity_all:
        if list_type[ele[0]] not in list_ignore:
            employee_writer.writerow([ele[0], ele[1], list_type[ele[0]]])

with open('result3.csv', mode='w') as write_list_entity:
    employee_writer = csv.writer(write_list_entity, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for ele in list_with_salience:
        if list_type[ele["name"]] not in list_ignore:
            employee_writer.writerow([ele['name'], ele['type'], ele['salience']])




