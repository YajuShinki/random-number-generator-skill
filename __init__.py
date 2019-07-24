from mycroft import MycroftSkill, intent_file_handler


class RandomNumberGenerator(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('generator.number.random.intent')
    def handle_generator_number_random(self, message):
        self.speak_dialog('generator.number.random')


def create_skill():
    return RandomNumberGenerator()

