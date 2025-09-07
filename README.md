flowchart TB
  SaaS[SaaS] -->|Provider ↑↑| ProviderSaaS[Infra + App + Runtime]
  SaaS -->|Customer ↑| CustomerSaaS[Data + Identity + Access]

  PaaS[PaaS] -->|Provider ↑↑| ProviderPaaS[Infra + Runtime]
  PaaS -->|Customer ↑↑| CustomerPaaS[Data + Identity + Config]

  IaaS[IaaS] -->|Provider ↑| ProviderIaaS[Infra (DC/Network/Hypervisor)]
  IaaS -->|Customer ↑↑↑| CustomerIaaS[OS + Apps + Config + Data + Identity]
