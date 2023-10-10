import argparse
import collections


class MindMap:
    def __init__(self):
        self.root = collections.defaultdict(list)

    def add_topic(self, topic, parent=None):
        if parent is None:
            self.root[topic] = []
        else:
            self.root[topic].append(parent)

    def add_subtopic(self, subtopic, parent_topic):
        self.root[parent_topic].append(subtopic)

    def display(self):
        for topic, subtopics in self.root.items():
            print(f"{topic}:")
            for subtopic in subtopics:
                print(f"  {subtopic}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", help="Tytuł mapy myśli")
    args = parser.parse_args()

    mind_map = MindMap()
    if args.title:
        mind_map.add_topic(args.title)

    while True:
        input_line = input()
        if input_line == "exit":
            break

        topic, parent = input_line.split(":")
        if parent == "":
            mind_map.add_topic(topic)
        else:
            mind_map.add_subtopic(topic, parent)

        mind_map.display()


if __name__ == "__main__":
    main()

