package sample.refactoring;

import java.util.*;


class Product {
    private int price;
    private int weight;

    public Product(int price, int weight) {
        this.price = price;
        this.weight = weight;
    }

    public int getPrice() {
        return price;
    }

    public int getWeight() {
        return weight;
    }
}

// Before
class Shop {
    private final String MAP_TOTAL_PRICE_KEY = "total";
    private final String MAP_TOTAL_WEIGHT_KEY = "weight";

    private List<Product> products;

    public Shop(Product... productList) {
        products = new ArrayList<Product>();

        for (Product product : productList) {
            products.add(product);
        }
    }

    public Map<String, Integer> productSummary() {
        Map<String, Integer> summary = new HashMap<String, Integer>();
        summary.put(MAP_TOTAL_PRICE_KEY, 0);
        summary.put(MAP_TOTAL_WEIGHT_KEY, 0);

        // calculate price and weight
        for (Product product : products) {
            int prevPrice = summary.get(MAP_TOTAL_PRICE_KEY);
            int prevWeight = summary.get(MAP_TOTAL_PRICE_KEY);

            summary.put(MAP_TOTAL_PRICE_KEY, prevPrice + product.getPrice());
            summary.put(MAP_TOTAL_WEIGHT_KEY, prevWeight + product.getWeight());
        }

        return summary;
    }
}

// After
class Shop1 {
    private final String MAP_TOTAL_PRICE_KEY = "total";
    private final String MAP_TOTAL_WEIGHT_KEY = "weight";

    private List<Product> products;

    public Shop1(Product... productList) {
        products = new ArrayList<Product>();

        for (Product product : productList) {
            products.add(product);
        }
    }

    public Map<String, Integer> productSummary() {
        Map<String, Integer> summary = new HashMap<String, Integer>();

        summary.put(MAP_TOTAL_PRICE_KEY, 0);
        summary.put(MAP_TOTAL_WEIGHT_KEY, 0);

        // calculate price
        for (Product product : products) {
            int prevPrice = summary.get(MAP_TOTAL_PRICE_KEY);
            summary.put(MAP_TOTAL_PRICE_KEY, prevPrice + product.getPrice());
        }

        // calculate weight
        for (Product product : products) {
            int prevWeight = summary.get(MAP_TOTAL_PRICE_KEY);
            summary.put(MAP_TOTAL_WEIGHT_KEY, prevWeight + product.getWeight());
        }

        return summary;
    }
}


class LoopSplit {
    public static void main(String[] args) {
        Shop shop = new Shop(new Product(100, 550), new Product(1000, 200));
        Shop shop1 = new Shop(new Product(100, 550), new Product(1000, 200));

        System.out.println(shop.productSummary());
        System.out.println(shop1.productSummary());

        assert shop.productSummary() == shop1.productSummary();
    }
}
