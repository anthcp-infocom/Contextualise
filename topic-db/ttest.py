from topicdb.core.models.topic import Topic
from topicdb.core.models.association import Association

acme = Topic(identifier='acme', name='Acme Corporation')
jane = Topic(identifier='jane', name='Jane')
john = Topic(identifier='john', name='John')
peter = Topic(identifier='peter', name='Peter')
mary = Topic(identifier='mary', name='Mary')

association1 = Association(src_topic_ref='acme',
                           src_role_spec='employer',
                           dest_topic_ref='jane',
                           dest_role_spec='employee',
                           instance_of='employment')