from kazoo.client import KazooClient
import logging
import sys
from kazoo.recipe.barrier import DoubleBarrier

def init_logger():
    logging.basicConfig()
    logger = logging.getLogger()

    h = logging.StreamHandler(sys.stdout)
    h.flush = sys.stdout.flush
    logger.addHandler(h)

    return logger


if __name__ == "__main__":
    numberOfServiceReplicas=2
    groupName="barrier_group"
    zkPath = "/"+groupName+"/barrier/g" + str(numberOfServiceReplicas)
    logger = init_logger()

    print("Max elements in the group "+(str(numberOfServiceReplicas)))

    zk =  KazooClient(hosts='zoo1:2181')
    zkb = DoubleBarrier(zk,zkPath,numberOfServiceReplicas)

    print("Starting the client")
    zk.start()
    print("Entering in the barrier and waiting for the group")
    zkb.enter()

    # Note, if you disable the leaving code the clients will no longer
    # wait in the barrier after the first time the group leaves it. 
    # This can be useful sometimes.
    print("leaving the barrier")
    zkb.leave()

    # finish
    zk.stop()
    print("bye")