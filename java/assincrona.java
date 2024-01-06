import java.util.concurrent.CompletableFuture;

public class assincrona {

    public static void main(String[] args) {
        CompletableFuture<Void> futuro = CompletableFuture.runAsync(() -> {
            System.out.println("Começando...");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("Olá, apos 1 segundo!");
        });

        futuro.join();
    }
}
