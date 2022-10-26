from unittest import TestLoader, TestSuite, TextTestRunner

from Orangechrmlive.Test.test_cases.test_Logo import TestLogo
from Orangechrmlive.Test.test_cases.test_employee import TestEmployee
from Orangechrmlive.Test.test_cases.test_Login import TestLogin

import testtools as testtools

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(TestLogo),
        loader.loadTestsFromTestCase(TestEmployee),
        loader.loadTestsFromTestCase(TestLogin)
    ))

    # run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

    # #run test parallel using concurrent_suite
    concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
    concurrent_suite.run(testtools.StreamResult())
