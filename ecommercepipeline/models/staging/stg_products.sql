SELECT 
product_id,
product_name,
price,
stock,
INITCAP(category::text) AS category
FROM {{ source('raw', 'products') }}
WHERE product_id IS NOT NULL