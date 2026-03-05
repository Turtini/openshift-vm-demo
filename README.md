# OpenShift VM Creation Demo

This guide walks through the process of creating a virtual machine using OpenShift Virtualization.

OpenShift Virtualization allows teams to run traditional virtual machines directly inside a Kubernetes platform, alongside containers and cloud-native workloads.

This demo is designed for learning and training purposes and shows the basic workflow used by engineers to create and run a VM inside OpenShift.

It is part of the **Turtini Training Loop**, a series of short operational guides focused on building practical infrastructure skills.

---

## Overview

In this demo we will:

1. Log into the OpenShift console
2. Navigate to the Virtualization section
3. Create a new virtual machine
4. Configure storage and networking
5. Launch the VM
6. Connect to the virtual machine console

Estimated time: **10–15 minutes**

---

## Architecture Overview

The virtual machine will run inside the Kubernetes cluster using OpenShift Virtualization.

```
User
│
▼
OpenShift Web Console
│
▼
OpenShift Virtualization
│
▼
Virtual Machine
│
▼
Persistent Storage + Networking
```

---

## Step 1 — Log into OpenShift

1. Open the OpenShift Web Console
2. Sign in with your cluster credentials
3. Switch to the **Developer** or **Administrator** perspective

You should now see the OpenShift dashboard.

---

## Step 2 — Navigate to Virtualization

From the left navigation menu:

1. Click **Virtualization**
2. Select **Virtual Machines**

This section allows you to create and manage virtual machines within the cluster.

---

## Step 3 — Create a Virtual Machine

Click **Create Virtual Machine**.

Choose **From Template** for the demo.

Example template:

* Red Hat Enterprise Linux
* Fedora
* Windows Server

Provide a name for the VM.

Example:

demo-vm

---

## Step 4 — Configure Resources

Set the VM resources.

Recommended demo settings:

CPU: 2
Memory: 4 GiB

These settings are sufficient for most demo workloads.

---

## Step 5 — Configure Storage

OpenShift will automatically provision storage for the VM disk.

Typical configuration:

* Persistent Volume Claim
* Container-native storage
* Cluster storage class

---

## Step 6 — Configure Networking

Use the default cluster network configuration.

The VM will receive a network interface connected to the OpenShift cluster network.

---

## Step 7 — Launch the VM

Click **Create Virtual Machine**.

The platform will begin provisioning the VM and attaching storage and networking.

Provisioning typically takes **30–90 seconds** depending on the cluster.

---

## Step 8 — Access the Console

From the Virtual Machines list:

1. Select the VM
2. Click **Console**

The console provides direct access to the operating system running inside the VM.

---

## Step 9 — Verify the VM

Log into the virtual machine using the credentials configured in the template.

Once logged in, run:

uname -a

This confirms the VM is running successfully inside the Kubernetes cluster.

---

## Demo Complete

You have successfully:

* Created a virtual machine inside OpenShift
* Provisioned storage and networking
* Accessed the VM console

---

## Related Demo

A companion guide shows how to create a virtual machine using Amazon Web Services.

Together these demos illustrate the difference between:

* Cloud-based virtual machines
* Virtual machines running inside Kubernetes

---

## About Turtini

Turtini builds operational platforms that make open source delivery seamless for federal teams.

Learn more:

https://turtini.com

