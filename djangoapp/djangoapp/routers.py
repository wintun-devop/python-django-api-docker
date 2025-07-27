

""" for one replica """
class ReplicaRouter:
    def db_read(self, model, **hints):
        return 'replica'

    def db_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'default'
    

""" for one more replica """
""" 
class ReplicaRouter:
    replica_dbs = ['replica1', 'replica2']

    def db_for_read(self, model, **hints):
        return random.choice(self.replica_dbs)

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'default'
"""
