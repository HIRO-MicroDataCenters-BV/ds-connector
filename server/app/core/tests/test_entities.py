from ..entities import Connector, DataProduct, Interface, Tag


class TestDataProduct:
    def test_common(self):
        data_product = DataProduct(
            id="dataproduct1",
            name="cancer_2020",
            size=2048,
            mimetype="text/plain",
            digest="4gf50e8ad219e34f0b911e097b7b588e31f9b435",
            tags=[
                Tag("tag1"),
                Tag("tag2"),
            ],
            source={
                "connector": Connector("connector1"),
                "interface": Interface("interface1"),
            },
            _links={
                "accessPoint": "http://example.com/access",
            },
        )

        assert data_product.id == "dataproduct1"
        assert data_product.name == "cancer_2020"
        assert data_product.size == 2048
        assert data_product.mimetype == "text/plain"
        assert data_product.digest == "4gf50e8ad219e34f0b911e097b7b588e31f9b435"
        assert len(data_product.tags) == 2
        assert data_product.tags[0].text == "tag1"
        assert data_product.tags[1].text == "tag2"
        assert data_product.source["connector"].id == "connector1"
        assert data_product.source["interface"].id == "interface1"
        assert data_product._links["accessPoint"] == "http://example.com/access"
