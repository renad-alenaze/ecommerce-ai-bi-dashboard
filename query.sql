SELECT
  CURRENT_DATE AS date,
  "Category",
  COUNT(*) AS total_orders,
  ROUND(SUM("Amount")::numeric, 2) AS total_sales,
  ROUND(AVG("Amount")::numeric, 2) AS avg_order_value
FROM supply_chain_inventory
GROUP BY "Category"
ORDER BY total_sales DESC;