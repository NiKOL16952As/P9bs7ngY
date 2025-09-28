# 代码生成时间: 2025-09-29 02:09:28
import requests
import psutil
import json

"""
Network Traffic Monitor

This script monitors network traffic using the psutil library to collect data and
requests library to make HTTP requests. It retrieves the current network traffic
statistics and provides an endpoint to access this data.
"""


class NetworkTrafficMonitor:
    def __init__(self):
        # Initialize network traffic data
        self.rx_bytes = 0
        self.tx_bytes = 0
        self.rx_packets = 0
        self.tx_packets = 0
        self.rx_errs = 0
        self.tx_errs = 0
        self.rx_drop = 0
        self.tx_drop = 0

    def collect_network_data(self):
        """Collect current network traffic data."""
        # Get network interface statistics
        stats = psutil.net_io_counters(pernic=True)
        
        # Update network traffic data
        for interface, data in stats.items():
            self.rx_bytes += data.bytes_recv
            self.tx_bytes += data.bytes_sent
            self.rx_packets += data.packets_recv
            self.tx_packets += data.packets_sent
            self.rx_errs += data.errin
            self.tx_errs += data.errout
            self.rx_drop += data.dropin
            self.tx_drop += data.dropout

    def get_network_traffic(self):
        """Return current network traffic data."""
        return {
            "rx_bytes": self.rx_bytes,
            "tx_bytes": self.tx_bytes,
            "rx_packets": self.rx_packets,
            "tx_packets": self.tx_packets,
            "rx_errs": self.rx_errs,
            "tx_errs": self.tx_errs,
            "rx_drop": self.rx_drop,
            "tx_drop": self.tx_drop
        }

    def start_monitoring(self):
        """Start monitoring network traffic."""
        # Collect initial network data
        self.collect_network_data()
        
        # Create a simple HTTP server to expose network traffic data
        from http.server import BaseHTTPRequestHandler, HTTPServer
        
        class RequestHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path == "/network_traffic":
                    # Send network traffic data as JSON
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(self.server.network_traffic).encode())
                else:
                    self.send_response(404)
                    self.end_headers()
                    
        try:
            # Run HTTP server on port 8000
            server_address = ('', 8000)
            httpd = HTTPServer(server_address, RequestHandler)
            httpd.network_traffic = self.get_network_traffic()
            httpd.serve_forever()
        except KeyboardInterrupt:
            # Stop server on keyboard interrupt
            print("Stopping server...")
            httpd.server_close()

if __name__ == "__main__":
    # Create a NetworkTrafficMonitor instance and start monitoring
    monitor = NetworkTrafficMonitor()
    monitor.start_monitoring()