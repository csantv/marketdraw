create table stock(
    id smallint generated always as identity primary key,
    symbol varchar(20) not null unique
);

create table market_closes(
    id bigint generated always as identity primary key,
    trading_date date not null,
    stock_id smallint not null references stock,
    last_price numeric(18, 6) not null,
    unrealized_gain numeric(18, 4) not null,
    daily_gain numeric(18, 4) not null,
    used boolean not null default false
);
