create table dailyStockMarket(
    ID int not null auto_increment,
    Symbol varchar(32) not null,
    priceDate datetime not null,
    openPrice decimal(19,4) null,
    highPrice decimal(19,4) null,
    lowPrice decimal(19,4) null,
    closePrice decimal(19,4) null,
    adjClosePrice decimal(19,4) null,
    Volume bigint null, primary key(ID)
)engine=InnoDB auto_increment = 1 default charset = utf8;
