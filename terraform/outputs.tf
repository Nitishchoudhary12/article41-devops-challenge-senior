output "load_balancer_dns" {
  value       = aws_lb.app.dns_name
  description = "Public DNS of the Application Load Balancer"
}
