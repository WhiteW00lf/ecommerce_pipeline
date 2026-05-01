SELECT 
    customer_id,
    first_name,
    last_name,
    address,
    loyalty_tier,
    last_updated
FROM
    {{ source('raw', 'customers') }}