import hug
import inflect
engine = inflect.engine()

@hug.get(versions=1)
def singular(word: hug.types.text):
  """ Return the singular version of the word """
  return engine.singular_noun(word).lower()

@hug.get(versions=1)
def plural(word: hug.types.text):
  """ Return the plural version of the word """
  return engine.plural(word).lower()


