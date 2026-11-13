const SUPABASE_URL = process.env.SUPABASE_URL || 'https://ukquyolgcstifhltvxku.supabase.co';
const SUPABASE_KEY = process.env.SUPABASE_KEY ||
  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVrcXV5b2xnY3N0aWZobHR2eGt1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njg3MjkxMjQsImV4cCI6MjA4NDMwNTEyNH0.XQj8RupAYwRpxFkkLJUohx_MM3zfC1ZMLnc-vJ4jYFQ';

module.exports = async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Headers', 'content-type');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  if (req.method === 'OPTIONS') {
    res.status(204).end();
    return;
  }
  if (req.method !== 'POST') {
    res.status(405).json({ ok: false, error: 'method not allowed' });
    return;
  }

  try {
    let body = req.body;
    if (Buffer.isBuffer(body)) body = body.toString('utf8');
    if (typeof body === 'string') body = JSON.parse(body);
    if (!body || typeof body !== 'object') {
      res.status(400).json({ ok: false, error: 'invalid body' });
      return;
    }

    const row = {
      name: String(body.name || '未填写').slice(0, 100),
      contact: String(body.contact || '未填写').slice(0, 200),
      target_school: String(body.target_school || '未填写').slice(0, 200),
      exam_year: parseInt(body.exam_year, 10) || 2027,
      info_json: body.info_json && typeof body.info_json === 'object' ? body.info_json : {},
      status: '待处理'
    };

    const r = await fetch(SUPABASE_URL + '/rest/v1/students', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        apikey: SUPABASE_KEY,
        Authorization: 'Bearer ' + SUPABASE_KEY,
        Prefer: 'return=minimal'
      },
      body: JSON.stringify(row)
    });

    if (!r.ok) {
      const detail = (await r.text()).slice(0, 300);
      res.status(502).json({ ok: false, error: detail || ('supabase ' + r.status) });
      return;
    }
    res.status(200).json({ ok: true });
  } catch (e) {
    res.status(500).json({ ok: false, error: String(e).slice(0, 300) });
  }
};
