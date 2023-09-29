#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/> .

from decouple import config

try:
    API_ID = config("API_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1449986020
    OWNER = config("OWNER")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -preset ultrafast -c:v libx265 -crf 27 -map 0:v -c:a aac -map 0:a -c:s copy -map 0:s? "{}"',
    )
except Exception as e:
    LOGS.info("Environment Vars Missing")
    LOGS.info("something Went Wrong")
    LOGS.info(str(e))
    exit(1)
