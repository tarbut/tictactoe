def start_database():
    from couchbase.cluster import Cluster
    from couchbase.cluster import PasswordAuthenticator
    cluster = Cluster('couchbase://localhost')
    authenticator = PasswordAuthenticator('couchbase', 'couchbase')
    cluster.authenticate(authenticator)
    return cluster