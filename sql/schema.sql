create table stock(
    id smallint generated always as identity primary key,
    symbol varchar(20) not null unique
);

create table market_closes(
    id bigint generated always as identity primary key,
    trading_date date not null,
    stock_id smallint not null references stock,
    allocation_pct numeric not null,
    last_price numeric not null,
    unrealized_gain numeric not null,
    daily_gain numeric not null,
    used boolean not null default false
);
