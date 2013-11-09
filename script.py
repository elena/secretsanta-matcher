import sys
import copy
from random import choice


def get_matches(name_list):
  matches = []
  pick_list = copy.deepcopy(name_list)

  def get_pick(name, pick_list):
    pick = choice(pick_list)
    print "... checking: {}, {}".format(name, pick)
    if pick != name:
      pick_list.remove(pick)
      print "Success!: {} {}".format(name, pick)
      print "remaining: {}\n ...".format(", ".join(pick_list))
      return (name, pick), pick_list
    else:
      print "... clash, try again."
      get_pick(name, pick_list)

  for name in name_list:
    print "matching {}".format(name)
    match, pick_list = get_pick(name, pick_list)
    matches.append((match))

  print matches
  return matches


def main(argv=sys.argv):
  arg_list = argv[1:]

  # convert args to csv
  print arg_list
  name_list = " ".join(arg_list).split(", ")
  try:
    name_list.remove("")
  except ValueError:
    pass

  if len(name_list) >= 2:
    return get_matches(name_list)
  else:
    print "Please enter at least 2 names."

if __name__ == '__main__':
  main()
