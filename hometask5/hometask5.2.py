class Course():
    """ Course """
    tasks = {}
    exam_score = 0
    lab_max = 1
    def_task_num = 0

    def __init__(self, course_config):
        self.exam_max = course_config["exam_max"]
        self.lab_max = course_config["lab_max"]
        self.lab_num = course_config["lab_num"]
        self.threshold = course_config["k"]


    def make_task(self, score: int, task_number: int = def_task_num):
        """make task from course"""
        if (task_number < self.lab_num) & (task_number >= 0):
            if (score <= self.lab_max) & (score >= 0):
                self.tasks.update({task_number: score})
                self.def_task_num = self.default_task_number()
        return self

    def default_task_number(self):
        """Determine default task number"""
        if len(self.tasks) <= self.lab_num:
            made_tasks = {k[0] for k in self.tasks.items()}
            rest_tasks = set(range(0, self.lab_num)).difference(made_tasks)
            if rest_tasks:
                return min(rest_tasks)
            else:
                return -1
        else:
            return -1

    def make_exam(self, score: int):
        if score <= self.exam_max:
            self.exam_score = score
        return self

    def sum_score(self):
        sum_score = 0
        for el in self.tasks.values():
            sum_score += el
        sum_score += self.exam_score
        return sum_score

    def is_certified(self):
        course_score = self.sum_score()
        exam_pass = course_score/(self.exam_max + self.lab_max*self.lab_num) >= self.threshold
        print(course_score/(self.exam_max + self.lab_max*self.lab_num))
        return (course_score, exam_pass)

    def get_def_task_num(self):
        return self.def_task_num


class Student():

    def __init__(self, name, course_config):
        self.name = name
        self.course_phyton = Course(course_config)

    def make_lab(self, m, n=None):
        if n is None:
            n = self.course_phyton.get_def_task_num()
        self.course_phyton.make_task(m, n)
        # print(self.course_phyton.tasks)

    def make_exam(self, m):
        self.course_phyton.make_exam(m)

    def is_certified(self):
        return self.course_phyton.is_certified()


conf = {
    "exam_max": 30,
    "lab_max": 7,
    "lab_num": 10,
    "k": 0.61
}

student1 = Student("George", conf)
student1.make_lab(5, 0)
student1.make_lab(5, 5)
student1.make_lab(5, 3)
student1.make_lab(5)
student1.make_lab(-15)
student1.make_lab(5)
student1.make_lab(5)
student1.make_lab(5)
student1.make_lab(1, 6)
student1.make_lab(5)
student1.make_lab(5)
student1.make_lab(1000)
student1.make_exam(23)
print(student1.course_phyton.tasks)
print(student1.is_certified())
