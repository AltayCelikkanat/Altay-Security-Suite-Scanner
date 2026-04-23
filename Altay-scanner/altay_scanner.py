import socket
from concurrent.futures import ThreadPoolExecutor

class AltayScannerEngine:
    """
    Altay Security Suite - Core Scanning Engine
    Yüksek performanslı, thread-pool tabanlı ağ tarama motoru.
    """
    
    def __init__(self, target_ip: str, max_threads: int = 100):
        self.target_ip = target_ip
        self.max_threads = max_threads
        self.open_ports = []

    def _scan_port(self, port: int) -> tuple:
        """Tekil port tarama fonksiyonu."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5) # Gecikme süresi (Latency)
                result = s.connect_ex((self.target_ip, port))
                if result == 0:
                    return port, True
        except Exception:
            pass
        return port, False

    def run_scan(self, port_range: tuple, callback=None):
        """
        Tarama işlemini ThreadPool ile başlatır.
        callback: Arayüze anlık veri göndermek için kullanılır (GUI entegrasyonu).
        """
        self.open_ports = []
        
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            # Port aralığını parçalara bölerek dağıt
            futures = {executor.submit(self._scan_port, port): port for port in range(port_range[0], port_range[1] + 1)}
            
            for future in futures:
                port, is_open = future.result()
                if is_open:
                    self.open_ports.append(port)
                    if callback:
                        callback(port) # Arayüzü güncellemek için sinyal gönder
        
        return self.open_ports