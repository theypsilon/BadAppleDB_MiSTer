#!/usr/bin/env python3
# Copyright (c) 2021 José Manuel Barroso Galindo <theypsilon@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# You can download the latest version of this tool from:
# https://github.com/theypsilon/BadAppleDB_MiSTer

import json
import time
from zipfile import ZipFile

def main():
    print('START!')

    make_db('bad_apple_full_res_db.json', 'data_full_res.txt', 0.07217318, 22*2)
    make_db('bad_apple_half_res_db.json', 'data_half_res.txt', 0.0925, 22*1)

def make_db(file_name, input, wait_time, height):
    db = {
        "db_id": 'bad_apple_db',
        "db_files": [],
        "files": {},
        "folders": {},
        "zips": {},
        "base_files_url": "",
        "default_options": {},
        "header": bad_apple_header(input, wait_time, height),
        "timestamp":  int(time.time())
    }

    save_json(db, file_name)

def bad_apple_header(input, wait_time, height):
    with open(input, 'rt') as fin:
        data = fin.read()

    header = []
    for page in data.split("SPLIT"):
        header.append('\033[H\033[2J')
        header.append(page + '\r')
        header.append(wait_time)
    
    header.append(2.0)
    header.append('\033[H\033[2J')

    page = ''
    for _ in range(int(height/2 - 4)):
        page += '\n'

    if height == 22:
        #       '                                                                                \n'
        page += '                                 by theypsilon                                  \n'
        page += '                                                                                \n'
        page += '                  based on github.com/Chion82/ASCII_bad_apple                   \n'

    else:
        #       '                                                                                                                                                                \n'
        page += '                                                                         by theypsilon                                                                          \n'
        page += '                                                                                                                                                                \n'
        page += '                                                          based on github.com/Chion82/ASCII_bad_apple                                                           \n'

    header.append(page)
    header.append(10.0)
    header.append('\033[H\033[2J')
    header.append('\n')

    return header

def save_json(db, json_name):
    zip_name = json_name + '.zip'
    with ZipFile(zip_name, 'w') as zipf:
        with zipf.open(json_name, "w") as jsonf:
            jsonf.write(json.dumps(db).encode("utf-8"))
    with open(json_name, 'w') as f:
        json.dump(db, f, sort_keys=True, indent=4)
    print('Saved ' + zip_name)

if __name__ == "__main__":
    main()
