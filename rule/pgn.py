class PGNLoader(object):
    def __init__(self):
        pass

    def load(self, file_name):
        with open(file_name) as file:
            flines = file.readlines()
        lines = []
        for line in flines:
            it = line.strip().decode("GBK")
            if len(it) == 0:
                continue
            lines.append(it)

        lines = self.__get_headers(lines)
        lines, docs = self.__get_comments(lines)
        self.infos["Doc"] = docs
        self.__get_steps(lines)

    def __get_headers(self, lines):

        index = 0
        for line in lines:

            if line[0] != "[":
                return lines[index:]

            if line[-1] != "]":
                raise Exception("Format Error on line %" % (index + 1))

            items = line[1:-1].split("\"")

            if len(items) < 3:
                raise Exception("Format Error on line %" % (index + 1))

            self.infos[str(items[0]).strip()] = items[1].strip()

            index += 1

    def __get_comments(self, lines):

        if lines[0][0] != "{":
            return (lines, None)

        docs = lines[0][1:]

        # 处理一注释行的情况
        if docs[-1] == "}":
            return (lines[1:], docs[:-1].strip())

        # 处理多行注释的情况
        index = 1

        for line in lines[1:]:
            if line[-1] == "}":
                docs = docs + "\n" + line[:-1]
                return (lines[index + 1:], docs.strip())

            docs = docs + "\n" + line
            index += 1

            # 代码能运行到这里，就是出了异常了
        raise Exception("Comments not closed")

    def __get_token(self, token_mode, lines):
        pass

    def __get_steps(self, lines, next_step=1):

        for line in lines:
            if line in ["*", "1-0", "0-1", "1/2-1/2"]:
                return

            print
            line
            items = line.split(".")

            if (len(items) < 2):
                continue
                raise Exception("format error")

            steps = items[1].strip().split(" ")
            print
            steps


# -----------------------------------------------------#

if __name__ == '__main__':
    pass
