class PGNLoader():
    def __init__(self):
        pass
        self.infos = {}
        self.steps=[]

    def load(self, file_name):
        with open(file_name) as file:
            flines = file.readlines()
            lines = []
            for line in flines:
                if len(line) == 0:
                    continue
                lines.append(line)
        lines = self.__get_headers(lines)
        lines, docs = self.__get_comments(lines)
        self.infos["Doc"] = docs
        self.__get_steps(lines)

    def __get_headers(self, lines):
        '''

        :param lines: 输入文件，提取头信息，返回走棋步骤
        :return:
        '''
        index = 0
        for line in lines:
            if line[0] != "[":
                return lines[index:]
            if line[-2] != "]":  # -1为换行符
                raise Exception("Format Error on line %d" % (index + 1))
            items = line[1:-2].split('"')
            if len(items) < 3:
                raise Exception("Format Error on line %d" % (index + 1))
            self.infos[str(items[0]).strip()] = items[1].strip()#去掉字符串多余空格
            index += 1

    def __get_comments(self, lines):
        if lines[0][0] != "{":
            return (lines, None)
        docs = lines[0][1:]
        # 处理一注释行的情况
        if docs[-2] == "}":
            return (lines[1:], docs[:-2].strip())
        # 处理多行注释的情况
        index = 1
        for line in lines[1:]:
            if line[-2] == "}":
                docs = docs + line[:-2]
                return (lines[index + 1:], docs.strip())
            docs = docs + line
            index += 1
        # 代码能运行到这里，就是出了异常了
        raise Exception("Comments not closed")

    def __get_steps(self, lines):

        for line in lines:
            if line in ["*", "1-0", "0-1", "1/2-1/2"]:
                return
            items = line.split(".")
            if (len(items) != 2):
                continue
            step = items[1].strip().split(" ")
            if self.steps.__len__()!=0:
                if self.steps[-1].__len__()==1:
                    self.steps[-1].append(step[0])
                    continue
            self.steps.append(step)


if __name__ == '__main__':
    pgnLoader = PGNLoader()
    pgnLoader.load(r"D:\Programme\MachineLearning\AphaZero_ChineseChess\data\pgn\135.PGN")
