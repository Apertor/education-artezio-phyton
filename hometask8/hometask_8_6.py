"""hometask 8.6"""
# Напишите шаблон регулярного выражения,
# который соответствует вопросительным
# предложениям, в которых одно слово (более 2 символов)
# повторяется 4 или более раз.

import re

#############################################
REGEX = r"^.*([a-zA-Z]{3,}).*\1.*\1.*\1.*\?$"
#############################################

TEST_STR = "odd yes od yes yd yes odd yes odd hello?"

MATCHES = re.finditer(REGEX, TEST_STR, re.MULTILINE)

for matchNum, match in enumerate(MATCHES, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}".
          format(matchNum=matchNum, start=match.start(),
                 end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".
              format(groupNum=groupNum, start=match.start(groupNum),
                     end=match.end(groupNum),
                     group=match.group(groupNum)))
