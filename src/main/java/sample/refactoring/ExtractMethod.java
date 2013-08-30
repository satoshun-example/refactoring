// Before

class PrintHtml {
    private final String head;
    private final String content;

    public PrintHtml(String head, String content) {
        this.head = head;
        this.content = content;
    }

    public void show() {
        System.out.println("<head>");
        System.out.println(head);
        System.out.println("</head>");

        System.out.println("<body>");
        System.out.println(content);
        System.out.println("</body>");
    }

    public String toString() {
        return getClass().getSimpleName();
    }
}

// After

class PrintHtml2 {
    private final String head;
    private final String content;

    public PrintHtml2(String head, String content) {
        this.head = head;
        this.content = content;
    }

    public void show() {
        showHead();
        showContent();
    }

    public void showHead() {
        System.out.println("<head>");
        System.out.println(head);
        System.out.println("</head>");
    }

    public void showContent() {
        System.out.println("<body>");
        System.out.println(content);
        System.out.println("</body>");
    }

    public String toString() {
        return getClass().getSimpleName();
    }
}


class ExtractMethod {
    public static void main(String[] args) {
        PrintHtml p = new PrintHtml("header", "My name is jun");
        PrintHtml2 p2 = new PrintHtml2("header", "My name is jun");

        System.out.println(p);
        p.show();
        System.out.println();
        System.out.println(p2);
        p2.show();
    }
}
