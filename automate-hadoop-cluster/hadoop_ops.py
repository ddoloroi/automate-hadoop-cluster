__author__ = 'rakesh.varma'

class hadoop:

    nameNode = None
    secondaryNamenode = None
    dataNodes = []
    home_dir = '/home/ubuntu/hadoop'

    def __init__(self, namenode, secondaryNamenode, dataNodes):
        self.nameNode = namenode
        self.secondaryNamenode = secondaryNamenode
        self.dataNodes = dataNodes

    @property
    def core_site_text(self):
        return """<?xml version=\\""1.0\\"" encoding=\\""UTF-8\\""?>
                        <?xml-stylesheet type=\\""text/xsl\\"" href=\\""configuration.xsl\\""?>
                        <configuration>
                        <property>
                        <name>fs.default.name</name>
                        <value>hdfs://{0}:8020</value>
                        </property>
                        <property>
                        <name>hadoop.tmp.dir</name>
                        <value>/home/ubuntu/hdfstmp</value>
                        </property>
                        </configuration>""".format(self.nameNode)

    @property
    def hdfs_site_text(self):
        return """<?xml version=\\""1.0\\"" encoding=\\""UTF-8\\""?>
                        <?xml-stylesheet type=\\""text/xsl\\"" href=\\""configuration.xsl\\""?>
                        <configuration>
                        <property>
                        <name>dfs.replication</name>
                        <value>2</value>
                        </property>
                        <property>
                        <name>dfs.permissions</name>
                        <value>false</value>
                        </property>
                        </configuration>"""

    @property
    def mapred_site_text(self):
        return """<?xml version=\\""1.0\\"" encoding=\\""UTF-8\\""?>
                        <?xml-stylesheet type=\\""text/xsl\\"" href=\\""configuration.xsl\\""?>
                        <configuration>
                        <property>
                        <name>mapred.job.tracker</name>
                        <value>hdfs://{0}:8021</value>
                        </property>
                        </configuration>""".format(self.nameNode)

    @property
    def config_dir(self):
        return self.home_dir + '/etc/hadoop'

    @property
    def config_coresite_path(self):
        return self.config_dir + '/core-site.xml'

    @property
    def config_hdfssite_path(self):
        return self.config_dir + '/hdfs-site.xml'

    @property
    def config_mapredsite_path(self):
        return self.config_dir + '/mapred-site.xml'

    @property
    def config_master_path(self):
        return self.config_dir + '/masters'

    @property
    def config_slave_path(self):
        return self.config_dir + '/slaves'
