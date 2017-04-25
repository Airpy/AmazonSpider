# 商品表
DROP TABLE IF EXISTS t_product;
CREATE TABLE t_product
(
  id                        BIGINT(20)           NOT NULL   AUTO_INCREMENT  COMMENT  '编号'
 ,productCode               VARCHAR(32)                                     COMMENT  '商品编码'
 ,state                     TINYINT(4)                                       COMMENT  '商品状态. 1: 正常; 0: 失效'
 ,chineseName               VARCHAR(128)                                    COMMENT  '商品中文名称'
 ,japanName                 VARCHAR(128)                                    COMMENT  '商品日文名称'
 ,imgUrl                    VARCHAR(256)                                    COMMENT  '商品图片URL地址'
 ,promotionFlag             TINYINT(4)                                       COMMENT  '促销标识. 1: 当前享有促销; 0: 当前无促销'
 ,seller                    TINYINT(4)                                       COMMENT  '卖家标识. 1: 自营; 2: 第三方货亚马逊销售; 3: 第三方'
 ,minPrice                  DECIMAL(24,2)                                   COMMENT  '历史最低价(不扣减积分)'
 ,PRIMARY KEY (id)
);


# 商品与价格关联表
DROP TABLE IF EXISTS t_product_price;
CREATE TABLE t_product_price
(
  id                        BIGINT(20)           NOT NULL   AUTO_INCREMENT  COMMENT  '编号'
 ,productId                 BIGINT(20)                                       COMMENT  '商品id'
 ,price                     DECIMAL(24,2)                                   COMMENT  '商品价格'
 ,pointFlag                 TINYINT(4)                                       COMMENT  '积分标识. 1: 当前享有积分; 0: 当前无积分'
 ,points                    INT(20)              DEFAULT 0                  COMMENT  '商品积分'
 ,totalPrice                DECIMAL(24,2)                                   COMMENT  '商品最后价格(price-points)'
 ,extractTime               DATETIME                                         COMMENT  '爬虫时间'
 ,PRIMARY KEY (id)
)