# Dify 天气查询工具 (FastAPI)

基于 [FastAPI](https://fastapi.tiangolo.com) 构建的天气查询服务，可作为 [Dify](https://dify.ai) 平台的自定义工具（Custom Tool）接入，为 LLM 应用提供实时天气数据调用能力。

## 技术栈

- **后端**: Python + FastAPI + SQLModel (ORM) + Pydantic
- **数据库**: PostgreSQL
- **前端**: React + TypeScript + Vite + Tailwind CSS + shadcn/ui
- **部署**: Docker Compose
- **测试**: Playwright (E2E) + Pytest

## 功能

- 天气查询 API：根据城市名返回天气状况和温度
- 用户认证：JWT Token 登录 / 注册
- 用户管理：超级管理员创建、权限控制
- Items CRUD：示例增删改查接口
- 自动生成 OpenAPI 文档（`/docs`），可直接导入 Dify 作为自定义工具
- Docker Compose 一键启动

## 快速启动

### 前置要求

- [Docker](https://www.docker.com/) + Docker Compose
- [Node.js](https://nodejs.org/) 18+（仅开发前端时需要）
- [Python](https://www.python.org/) 3.10+（仅本地开发时需要）

### 1. 配置环境变量

```bash
cp .env.example .env
# 编辑 .env，填写你的数据库密码等信息
```

### 2. Docker Compose 启动

```bash
docker compose up -d
```

启动完成后：

| 服务 | 地址 |
|------|------|
| 后端 API 文档 (Swagger) | http://localhost:8000/docs |
| 前端页面 | http://localhost:5173 |
| PostgreSQL | localhost:5432 |
| Mailpit (邮件测试) | http://localhost:8025 |

## API 文档

### 天气查询

```
GET /api/v1/get_weather?city={城市名}
```

**参数**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| city | string | 是 | 城市名，如 "北京" |

**响应示例**

```json
{
  "city": "北京",
  "weather": "晴",
  "temperature": 25
}
```

### 其他接口

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/v1/login/access-token` | 登录获取 Token |
| POST | `/api/v1/users/` | 注册用户 |
| GET | `/api/v1/users/` | 获取用户列表（需管理员权限） |
| GET/POST | `/api/v1/items/` | Items 增删改查 |

完整交互式 API 文档请访问 http://localhost:8000/docs

## 接入 Dify

1. 启动服务后，打开 Dify 控制台
2. 进入「工具」→「自定义」→「创建自定义工具」
3. 导入 OpenAPI Schema：填入 `http://localhost:8000/openapi.json`（或手动粘贴）
4. 配置鉴权方式（如需认证，使用 Bearer Token）
5. 在 Dify 应用的 Agent 编排中添加该工具，LLM 即可自动调用天气查询

## 项目结构

```
full-stack-fastapi/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   ├── weather.py    # 天气查询接口
│   │   │   │   ├── login.py      # 认证
│   │   │   │   ├── users.py      # 用户管理
│   │   │   │   └── items.py      # CRUD 示例
│   │   │   └── main.py           # 路由注册
│   │   ├── core/                 # 配置、安全、中间件
│   │   ├── models.py             # 数据模型
│   │   └── main.py               # 应用入口
│   ├── tests/                    # 测试
│   └── pyproject.toml
├── frontend/                     # React 前端
├── compose.yml                   # Docker Compose 配置
├── .env.example                  # 环境变量模板
└── README.md
```

## 本地开发

```bash
# 安装后端依赖
cd backend
uv sync

# 启动开发服务器（热重载）
uv run uvicorn app.main:app --reload

# 安装前端依赖
cd frontend
bun install
bun run dev
```

## License

MIT
