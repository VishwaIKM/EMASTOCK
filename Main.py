import Configuration as conf
class Initializer:
    def Run():
        conf.Config.LoadConfig() ## LOAD CONFIG

if __name__ == '__main__':
    Initializer.Run()