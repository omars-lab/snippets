import unittest


class Tester(unittest.TestCase):

    def test_zip(self):
        """
        zip takes to arrays and makes an array of tuples where tuple 1 is a
        tuple composed of element 1 of array 1 and 2, etc...
        """
        # combines to arrays into one array of tuples
        self.assertEqual(
            zip(sorted(set('qwerty')), sorted(set('asdfgh'))),
            [('e', 'a'), ('q', 'd'), ('r', 'f'),
             ('t', 'g'), ('w', 'h'), ('y', 's')]
        )

        questions = ['name', 'quest', 'favorite color', "WILL GET SKIPPED"]
        answers = ['lancelot', 'the holy grail', 'blue']
        self.assertEqual(
            zip(questions, answers),
            [('name', 'lancelot'), ('quest', 'the holy grail'),
             ('favorite color', 'blue')]
        )

        a = [1, 2]
        b = [(1), (2)]
        c = [(1,), (2,)]
        d = [(1, 1), (2, 2)]

        self.assertEquals(
            zip(a, d),
            zip(b, d),
            [(1, (1, 1)), (2, (2, 2))]
        )

        self.assertEquals(
            zip(a, b),
            [(1, 1), (2, 2)],
        )

        self.assertEquals(
            zip(a, c),
            zip(b, c),
            [(1, (1,)), (2, (2,))],
        )

        self.assertEquals(
            zip(c, d),
            [((1,), (1, 1)), ((2,), (2, 2))],
        )

    def test_any(self):
        """
        any([array])
            => takes an array and returns true if any of the elements are true
        """
        self.assertEquals(any([True, False]), True)
        self.assertEquals(any([None, "apple"]), True)

        self.assertEquals(any([False, False]), False)
        self.assertEquals(any([None, ""]), False)

    def test_enumerate_and_string_sets(self):
        """
        * set('string') => returns a set of the charcacters of the string,
            it also skips any duplicate characters.
        * enumerate(<list>) => returns a list of the following nature:
            [(1, <first_element_of_list>), ..., (N, <Nth_element_of_list>)]
        * <dict>.items() => returns a list of the following nature:
            [(key, value), ...]
        """
        # generates an itterator that returns [(index, value), ....]
        char_list = [(index, v) for index, v in enumerate(sorted(set('abca')))]
        self.assertEquals(
            {0: "a", 1: 'b', 2: 'c'}.items(),
            char_list
        )

    def test_reverse_enumerate_and_string_sets(self):
        self.assertEquals(
            [x for x in reversed(sorted(set(('aceg'*4) + ('bdfh'*3))))],
            list(reversed(sorted(set('abcdefgh'))))
        )

if __name__ == "__main__":
    unittest.main()
