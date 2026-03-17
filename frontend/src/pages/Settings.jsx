import { useAuth } from '../context/AuthContext';
import { Settings as SettingsIcon, User, Bell, Palette } from 'lucide-react';

export default function SettingsPage() {
  const { user } = useAuth();
  const role = user?.role === 'it_manager' ? 'IT Manager' : user?.role?.charAt(0).toUpperCase() + user?.role?.slice(1);

  return (
    <div style={{ maxWidth: 700, margin: '0 auto' }}>
      <div style={{ marginBottom: 28 }}>
        <h1 style={{ fontSize: 24, fontWeight: 700, color: '#fff', display: 'flex', alignItems: 'center', gap: 10 }}>
          <SettingsIcon style={{ width: 24, height: 24, color: '#6b6b8a' }} /> Settings
        </h1>
        <p style={{ fontSize: 13, color: '#6b6b8a', marginTop: 4 }}>Manage your account and preferences</p>
      </div>

      {/* Profile */}
      <div className="glass-strong" style={{ padding: 24, marginBottom: 18 }}>
        <h2 style={{ fontSize: 15, fontWeight: 600, color: '#fff', marginBottom: 20, display: 'flex', alignItems: 'center', gap: 8 }}>
          <User style={{ width: 18, height: 18, color: '#8b5cf6' }} /> Profile
        </h2>
        <div style={{ display: 'flex', alignItems: 'center', gap: 16, marginBottom: 24 }}>
          <div style={{
            width: 56, height: 56, borderRadius: '50%',
            background: 'linear-gradient(135deg, #8b5cf6, #06b6d4)',
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            color: '#fff', fontSize: 22, fontWeight: 700,
          }}>{user?.name?.charAt(0)?.toUpperCase()}</div>
          <div>
            <div style={{ fontSize: 17, fontWeight: 700, color: '#fff' }}>{user?.name}</div>
            <div style={{ fontSize: 13, color: '#6b6b8a' }}>{user?.email}</div>
            <span style={{ fontSize: 11, padding: '3px 10px', borderRadius: 6, background: 'rgba(139,92,246,0.12)', color: '#a78bfa', fontWeight: 600, marginTop: 6, display: 'inline-block' }}>{role}</span>
          </div>
        </div>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 14 }}>
          {[{ l: 'Full Name', v: user?.name }, { l: 'Email', v: user?.email }, { l: 'Department', v: user?.department || '—' }, { l: 'Role', v: role }].map(f => (
            <div key={f.l}>
              <label style={{ display: 'block', fontSize: 12, color: '#9494b0', marginBottom: 6, fontWeight: 500 }}>{f.l}</label>
              <input className="input" value={f.v || ''} readOnly style={{ opacity: 0.7 }} />
            </div>
          ))}
        </div>
      </div>

      {/* Notifications */}
      <div className="glass-strong" style={{ padding: 24, marginBottom: 18 }}>
        <h2 style={{ fontSize: 15, fontWeight: 600, color: '#fff', marginBottom: 16, display: 'flex', alignItems: 'center', gap: 8 }}>
          <Bell style={{ width: 18, height: 18, color: '#f59e0b' }} /> Notifications
        </h2>
        {['Email notifications', 'Asset assignment alerts', 'Issue update alerts', 'Maintenance reminders'].map(item => (
          <div key={item} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '10px 0', borderBottom: '1px solid rgba(255,255,255,0.03)' }}>
            <span style={{ fontSize: 13, color: '#c0c0d4' }}>{item}</span>
            <div style={{
              width: 38, height: 20, borderRadius: 10, background: 'rgba(139,92,246,0.3)',
              position: 'relative', cursor: 'pointer',
            }}>
              <div style={{
                position: 'absolute', right: 2, top: 2, width: 16, height: 16, borderRadius: '50%',
                background: '#8b5cf6', transition: 'all 0.2s',
              }} />
            </div>
          </div>
        ))}
      </div>

      {/* Appearance */}
      <div className="glass-strong" style={{ padding: 24 }}>
        <h2 style={{ fontSize: 15, fontWeight: 600, color: '#fff', marginBottom: 12, display: 'flex', alignItems: 'center', gap: 8 }}>
          <Palette style={{ width: 18, height: 18, color: '#06b6d4' }} /> Appearance
        </h2>
        <p style={{ fontSize: 13, color: '#6b6b8a' }}>Dark theme is the default and only available theme.</p>
      </div>
    </div>
  );
}
