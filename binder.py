import os
import shutil

# from playsound import playsound


class Batou():
    """
    Creates directories and files.
    """

    def create_dir(self, dir_name, logger):
        """
        """

        if not os.path.exists(dir_name):
            print("Creating directory...")
            logger.info("Creating directory...")
            path = os.path.join(os.getcwd(), dir_name)
            os.mkdir(path)
            print("{0} has been created.".format(dir_name))
            logger.info("{0} has been created.".format(dir_name))

        else:
            print("Gerty, am I a clone?")
            logger.info("Gerty, am I a clone?")
            print("{0} already exists.".format(dir_name))
            logger.info("{0} already exists.".format(dir_name))
            print("To continue, rename or go to another directory.")
            logger.info("To continue, rename or go to another directory.")

    def create_file(self, file_name, content, logger):
        """
        """

        if not os.path.exists(file_name):
            print("Creating file...")
            logger.info("Creating file...")
            file = open(file_name, "w")
            file.write(content)
            file.close()
            print("{0} has been created.".format(file_name))
            logger.info("{0} has been created.".format(file_name))

        else:
            print("Gerty, am I a clone?")
            logger.info("Gerty, am I a clone?")
            print("{0} already exists.".format(file_name))
            logger.info("{0} already exists.".format(file_name))
            print("To continue, rename or go to a different directory.")
            logger.info("To continue, rename or go to a different directory.")


class Togusa():
    """
    Opens files.
    """

    def open_text_file(self, file_name, logger):
        """
        """

        print("Opening file...")
        logger.info("Opening file...")
        if os.path.exists(file_name):
            f = open(file_name, "r")
            print(f.read())
            logger.info(f.read())

        else:
            print("I'm sorry, Dave. I'm afraid I can't do that.")
            logger.info("I'm sorry, Dave. I'm afraid I can't do that.")
            print("{0} does not exist.".format(file_name))
            logger.info("{0} does not exist.".format(file_name))
            print("To continue, try a different name or directory.")
            logger.info("To continue, try a different name or directory.")

    # def open_mp3_file(self, mp3_name, logger):
    #     """
    #     """

    #     print("Playing mp3...")
    #     logger.info("Playing mp3...")
    #     song = mp3_name
    #     if os.path.exists(song):
    #         playsound(song + ".mp3")

    #     else:
    #         print("I'm sorry, Dave. I'm afraid I can't do that.")
    #         logger.info("I'm sorry, Dave. I'm afraid I can't do that.")
    #         print("{0} does not exist.".format(mp3_name))
    #         logger.info("{0} does not exist.".format(mp3_name))
    #         print("To continue, try a different name or directory.")
    #         logger.info("To continue, try a different name or directory.")


class Ishikawa():
    """
    Renames directories and files.
    """

    def rename_dir(self, old_dir_name, new_dir_name, logger):
        """
        """

        print("Renaming directory...")
        logger.info("Renaming directory...")
        source = old_dir_name
        destination = new_dir_name
        if os.path.exists(source):
            os.rename(source, destination)
            print("{0} has been renamed.".format(source))
            logger.info("This directory has been renamed.".format(source))

        elif not os.path.exists(source):
            print("Whatever it's called, it's someplace beautiful.")
            logger.info("Whatever it's called, it's someplace beautiful.")
            print("{0} cannot be found.".format(source))
            logger.info("{0} cannot be found.".format(source))
            print("To continue, try a different name or directory.")
            logger.info("To continue, try a different name or directory.")

        elif os.path.exists(destination):
            print("I think they want us to come and find them.")
            logger.info("I think they want us to come and find them.")
            print("{0} is somewhere else.".format(destination))
            logger.info("{0} is somewhere else.".format(destination))
            print("To continue, try a different name or directory.")
            logger.info("To continue, try a different name or directory.")

    def rename_file(self, old_file_name, new_file_name, logger):
        """
        """

        print("Renaming file...")
        logger.info("Renaming file...")
        source = old_file_name
        destination = new_file_name
        if os.path.exists(source):
            os.rename(source, destination)
            print("{0} has been renamed.".format(source))
            logger.info("{0} has been renamed.".format(source))

        elif not os.path.exists(source):
            print("I'm sorry, Dave. I'm afraid I can't do that.")
            logger.info("I'm sorry, Dave. I'm afraid I can't do that.")
            print("{0} does not exist.".format(source))
            logger.info("{0} does not exist.".format(source))
            print("To continue, try a different name or directory.")
            logger.info("To continue, try a different name or directory.")

        elif os.path.exists(destination):
            print("Brand. Shes...out there.")
            logger.info("Brand. She's...out there.")
            print("{0} already exists.".format(destination))
            logger.info("{0} already exists.".format(destination))
            print("To continue, try a different name or directory.")
            logger.info("To continue, try a different name or directory.")


class Pazu():
    """
    Copies files.
    """

    def copy_file(self, file_name, dir_name, logger):
        """
        """

        print("Copying file...")
        logger.info("Copying file...")
        source = file_name
        destination = dir_name
        if os.path.isfile(source):
            shutil.copy2(source, destination)
            print("{0} has been copied.".format(source))
            logger.info("{0} has been copied.".format(source))

        elif os.path.isdir(source):
            print("I'm sorry, Dave. I'm afraid I can't do that.")
            logger.info("I'm sorry, Dave. I'm afraid I can't do that.")
            print("{0} is not a file.".format(source))
            logger.info("{0} is not a file.".format(source))
            print("To continue, try a different name or directory.")
            logger.info("To continue, try a different name or directory.")

        else:
            print("Gerty, am I a clone?")
            logger.info("Gerty, am I a clone?")
            print("{0} is already there.".format(source))
            logger.info("{0} is already there.".format(source))
            print("To continue, rename or go to another directory.")
            logger.info("To continue, rename or go to another directory.")


class Boma():
    """
    Moves files.
    """

    def move_file(self, old_dir, file_name, new_dir, logger):
        """
        """

        print("Moving file...")
        logger.info("Moving file...")
        source = old_dir
        file = "/home/deepspaceghost/dev/prometheus/main/" + file_name
        destination = new_dir
        if os.path.exists(file):
            if os.path.exists(destination):
                shutil.copy2(file, destination)
                os.remove(file)
                print("{0} has been moved.".format(file))
                logger.info("{0} has been moved.".format(file))

            elif not os.path.exists(destination):
                os.mkdir(destination)
                shutil.copy2(file, destination)
                os.remove(file)
                print("{0} has been moved.".format(file))
                logger.info("{0} has been moved.".format(file))

            elif not os.path.isdir(source):
                print("I'm sorry, Dave. I'm afraid I can't do that.")
                logger.info("I'm sorry, Dave. I'm afraid I can't do that.")
                print("{0} is not a directory.".format(file))
                logger.info("{0} is not a directory.".format(file))
                print("To continue, try a different name or directory.")
                logger.info("To continue, try a different name or directory.")

        elif not os.path.exists(file):
            print("I'm sorry, Dave. I'm afraid I can't do that.")
            logger.info("I'm sorry, Dave. I'm afraid I can't do that.")
            print("{0} does not exist.".format(file))
            logger.info("{0} does not exist.".format(file))
            print("To continue, try a different name or directory.")
            logger.info("To continue, try a different name or directory.")


class Saito():
    """
    Deletes directories and files.
    """

    def delete_dir(self, dir_name, logger):
        """
        """

        print("Deleting directory...")
        logger.info("Deleting directory...")
        if os.path.isdir(dir_name):
            os.rmdir(dir_name)
            print("{0} has been deleted.".format(dir_name))
            logger.info("{0} has been deleted.".format(dir_name))

        else:
            print("I'm sorry, Dave. I'm afraid I can't do that.")
            logger.info("I'm sorry, Dave. I'm afraid I can't do that.")
            print("{0} does not exist.".format(dir_name))
            logger.info("{0} does not exist.".format(dir_name))
            print("To continue, try a different name or directory.")
            logger.info("To continue, try a different name or directory.")

    def delete_file(self, file_name, logger):
        """
        """

        print("Deleting file...")
        logger.info("Deleting file...")
        if os.path.isfile(file_name):
            os.remove(file_name)
            print("{0} has been deleted.".format(file_name))
            logger.info("{0} has been deleted.".format(file_name))

        else:
            print("I'm sorry, Dave. I'm afraid I can't do that.")
            logger.info("I'm sorry, Dave. I'm afraid I can't do that.")
            print("{0} does not exist.".format(file_name))
            logger.info("{0} does not exist.".format(file_name))
            print("To continue, try a different name or directory.")
            logger.info("To continue, try a different name or directory.")


class Azuma():
    """
    Finds files.
    """

    # if file.endswith('.txt'):

    def find_file(self, file_name, logger):
        """
        """

        print("Looking for file...")
        logger.info("Looking for file...")
        file = file_name
        dir_path = os.path.dirname(os.path.realpath(__file__))
        for root, dirs, files in os.walk(dir_path):
            if file in files:
                print(root + "/" + str(file))

    # def find_game(self, game_key, logger):
    # """
    # still needs work
    # """

    # print("Looking for game...")
    # logger.info("Looking for game...")
    # game = game_key
    # gamedex = {"inside": "18.06.28"}
    # for x in gamedex:
    #     if x in gamedex:
    #         print("Here is what we know: {0}".format(gamedex{}))
    #         logger.info("Here is what we know: " + print(gamedex{}))

    #     elif x not in gamedex:
    #         print("Whatever it's called, it's someplace beautiful.")
    #         logger.info("Whatever it's called, it's someplace beautiful.")
    #         print("{0} could not be found.".format(filename))
    #         logger.info("{0} could not be found.".format(filename))
    #         print("To continue, try a different name or directory.")
    #         logger.info("To continue, try a different name or directory.")
