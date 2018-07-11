# vertli 2018


class QuestionBank:

    # __init__: QeustionBank -> None
    def __init__(self):
        self.__question = []
        self.__choice = []
        self.__answer = []

    # file_open: String -> None
    def file_open(self, filename):
        try:
            file = open(filename, 'r', encoding="utf-8")
            str_list = file.readlines()
            list_len = len(str_list)
            for i in range(0, list_len, 8):
                self.set_question(str_list[i][:-1])
                self.set_choice(str_list[i+1][:-1],
                                str_list[i+2][:-1],
                                str_list[i+3][:-1],
                                str_list[i+4][:-1],
                                str_list[i+5][:-1])
                self.set_answer(str_list[i+6][:-1])
        except FileNotFoundError:
            print("Oops! I can't found the file {0} ._.".format(filename))
        except:
            print("Oops! File {0} opened unsuccessful...".format(filename))
        else:
            print("File {0} opened successful!".format(filename))

    # set_question: String -> None
    def set_question(self, question):
        self.__question.append(question)

    # get_question: Int -> String
    def get_question(self, index):
        return self.__question[index]

    # set_choice: String String String String String -> None
    def set_choice(self, a, b, c, d, e):
        choice_list = [a, b, c, d, e]
        self.__choice.append(choice_list)

    # get_choice_a: Int -> String
    def get_choice_a(self, index):
        return self.__choice[index][0]

    # get_choice_b: Int -> String
    def get_choice_b(self, index):
        return self.__choice[index][1]

    # get_choice_c: Int -> String
    def get_choice_c(self, index):
        return self.__choice[index][2]

    # get_choice_d: Int -> String
    def get_choice_d(self, index):
        return self.__choice[index][3]

    # get_choice_e: Int -> String
    def get_choice_e(self, index):
        return self.__choice[index][4]

    # set_answer: Char -> None
    def set_answer(self, answer):
        self.__answer.append(answer)

    # get_answer: Int -> Char
    def get_answer(self, index):
        return self.__answer[index]

    # __len__: None -> Int
    def __len__(self):
        return len(self.__question)
