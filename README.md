flowchart LR
  %% Shared Responsibility Model: Provider vs Customer across AWS, Azure, GCP
  subgraph AWS[Amazon Web Services]
    AProv[Provider\n• Physical DCs & Facilities\n• Network & Hypervisor\n• Managed Service Platform]:::prov
    ACust[Customer\n• Data & Identity (IAM)\n• OS/Apps/Configs (IaaS)\n• Access Controls & Keys\n• Compliance-in-Cloud]:::cust
  end

  subgraph AZ[Microsoft Azure]
    ZProv[Provider\n• Physical DCs & Facilities\n• Network & Hypervisor\n• PaaS/SaaS Runtime]:::prov
    ZCust[Customer\n• Data & Identity (Entra ID)\n• Workloads/Configs (IaaS)\n• RBAC/Policies/Keys\n• Compliance-in-Cloud]:::cust
  end

  subgraph GCP[Google Cloud Platform]
    GProv[Provider\n• Physical DCs & Facilities\n• Network & Hypervisor\n• Global Control Plane]:::prov
    GCust[Customer\n• Data & Identity (IAM)\n• Workloads/Configs (IaaS)\n• Org Policies/Keys\n• Compliance-in-Cloud]:::cust
  end

  classDef prov fill:#eef7ff,stroke:#1f6feb,stroke-width:1.5px,color:#0b3563
  classDef cust fill:#f5fff0,stroke:#1a7f37,stroke-width:1.5px,color:#0b3b19

  %% Notes: SaaS -> Provider takes more; IaaS -> Customer takes more
  note over AWS,AZ,GCP
    SaaS: Provider handles app & runtime; you own data + access.\n
    PaaS: Shared at runtime/config layers; you own data + access.\n
    IaaS: You manage OS, apps, configs; provider does physical/infra.
  end
