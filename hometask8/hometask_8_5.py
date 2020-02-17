"""hometask 8.5"""
#   Напишите шаблон регулярного выражения, который соответствовал бы паролю,
#   состоящему из 8-12 символов,
#   среди которых могут быть строчные и заглавные буквы латинского
#   алфавита, цифры, нижнее подчеркивание, звездочка, процент и амперсанд.
#   Пароль обязательно должен включать в себя одну строчную букву,
#   одну заглавную букву и одну цифру.


import re

########################################################
REGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[\w*%&]{8,12}$"
########################################################

TEST_STR = ("YYY1YDDT\n"
            "20200As21pss\n"
            "20Sd08_*&%")

MATCHES = re.finditer(REGEX, TEST_STR, re.MULTILINE)

for matchNum, match in enumerate(MATCHES, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}"
          .format(matchNum=matchNum, start=match.start(),
                  end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".
              format(groupNum=groupNum, start=match.start(groupNum),
                     end=match.end(groupNum),
                     group=match.group(groupNum)))
