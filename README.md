# 🛡️ API Security Validator (DevSecOps Pipeline)

Este repositório apresenta uma implementação prática de **DevSecOps**, utilizando **Python** e **GitHub Actions** para automatizar a validação de camadas de segurança em endpoints de API.

## 🚀 O Projeto
O objetivo é garantir que as APIs (especialmente em ambientes de integração como Fluig e Datasul) sigam as melhores práticas de segurança, verificando a presença de headers HTTP essenciais que protegem contra ataques comuns.

[Image of DevSecOps lifecycle diagram]

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **CI/CD:** GitHub Actions (Automação de Pipeline)
* **Biblioteca:** `requests` para interação com protocolos HTTP.

## ⚙️ Como a Automação Funciona (CI/CD)
Toda vez que um novo código é enviado para este repositório (`git push`):
1. O **GitHub Actions** dispara um container Linux (Ubuntu).
2. O ambiente Python é configurado automaticamente.
3. O script `scan.py` é executado para validar a URL configurada.
4. O resultado (Sucesso ou Alerta) é exibido diretamente nos logs da aba **Actions**.

## 📊 Por que isso é importante?
No dia a dia de um **Analista de Sistemas**, garantir que as comunicações entre sistemas externos e plataformas internas sejam seguras é fundamental. Este projeto demonstra como integrar essa preocupação diretamente no ciclo de desenvolvimento (Shift-Left Security).

---
✨ Desenvolvido por **Murilo Cardoso** | Estudante de ADS e Desenvolvedor.
