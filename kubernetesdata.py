from pywebio.input import *
from pywebio.output import *


def kubernetes():
    c = 0
    count = 0

    # Dictionary that stores questions and answers. Key is the correct answer. (format : ans : [question, options])
    dict = {'kubectl run': ["Command to run a pod?", 'kubectl run', 'kubectl inject', 'kubectl rollout', "kubectl input"],
            'redis': ["Choose the wrong kubernetes component?", 'apiserver', 'etcd', 'redis',
                            "kubelet"],
            'apps/v1': ["Kubernetes deployment api version?", 'v2', 'apps/v1',
                                        'apps/v3', "beta/v1"],

            # Add more questions are per Requirement

            }

    # Adding the extracted dictionart data to radio button
    for key, value in dict.items():

        x = value
        y = key

        q1 = radio(x[0], [x[1], x[2], x[3], x[4]], required=True)
        if q1 == y:
            c += 1  # to count the correct answer
        count += 1  # to count total questions

    return c, count  # returnig these count to main function
