import string
from collections import Counter

def word_count(paragraph):

    paragraph = paragraph.lower()
    paragraph = paragraph.translate(str.maketrans('','',string.punctuation))
    wordList = paragraph.split()
    counter = Counter(wordList)
    return counter



def main():

    paragraph = """A photo essay is a collection of images that work together to tell a story. 
    As we’ve seen, while photos are often considered incapable of lying because they “quote” from reality rather than altering it, pictures by themselves in isolation (both in time and space) are also often ambiguous and necessarily incomplete. 
    Over time, the subjects of photos become distant and alien to their viewers. 
    John Berger suggests that by creating stories with pictures, we can remedy such ambiguity and alienation by re-creating a “living context” that establishes a field of meaning that makes the photos come to life.
    Unlike typical stories (say a written, oral, or video story), however, photo essays can’t provide continuous, seamless narrative meaning, since they are composed of single and “frozen” snapshots.  Therefore, the connections between images are always to a certain degree jarring and surprising. 
    It is your job in this photo essay to compose a story that capitalizes on such surprise by helping the viewer see and build connections between your images. Together, they should contribute to a complex web of meaning that stimulates reflection on your topic and shows the things presented in a new and revealing light."""

    print(word_count(paragraph))


if __name__ == "__main__":
    main()